import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import os.path

class LstmModel:

    def prediction_LSTM(dict_price,name):
        dataframe_avg_price = pd.DataFrame(dict_price)
        #print("dataframe_avg_price",dataframe_avg_price)
        data_training = dataframe_avg_price[dataframe_avg_price['date']< pd.to_datetime('2020-7-01') ].copy()
        #print("data_training",data_training)
        data_test = dataframe_avg_price[dataframe_avg_price['date']>= pd.to_datetime('2020-7-01') ].copy()
        #print("data_test",data_test)

        data_training = data_training.drop(['date'],axis=1)
        #print("training_data",training_data.shape)

        scaler = MinMaxScaler()
        training_data = scaler.fit_transform(data_training)
        print("training_data",training_data.shape)

        X_train = []
        y_train = []

        for i in range(60,training_data.shape[0]):
            X_train.append(training_data[i-60:i])
            y_train.append(training_data[i,0])

        X_train,y_train = np.array(X_train),np.array(y_train)
        print("X_train",X_train.shape[1],"y_train",y_train.shape)

        ###prepare test dataset
        past_60_days = data_training.tail(60)
        print("past_days",past_60_days)
        df = past_60_days.append(data_test,ignore_index = True)
        df = df.drop(['date'],axis = 1)
        #print(df.head())
        inputs = scaler.fit_transform(df)
        X_test = []
        y_test = []
        for i in range(60,inputs.shape[0]):
            X_test.append(inputs[i-60:i])
            y_test.append(inputs[i,0])

        X_test,y_test = np.array(X_test),np.array(y_test)

        ###Building LSTM
        from tensorflow.keras import Sequential
        from tensorflow.keras.layers import Dense,LSTM,Dropout

        model = Sequential()

        model.add(LSTM(units = 60,activation = 'relu',return_sequences = True, input_shape = (X_train.shape[1],1)))
        model.add(Dropout(0.2))

        model.add(LSTM(units = 60,activation = 'relu',return_sequences = True))
        model.add(Dropout(0.2))

        model.add(LSTM(units = 80,activation = 'relu',return_sequences = True))
        model.add(Dropout(0.2))

        model.add(LSTM(units = 120,activation = 'relu'))
        model.add(Dropout(0.2))

        model.add(Dense(units=1))

        model.summary()

        model.compile(optimizer = 'Adam', loss = 'mean_squared_error')
        model.fit(X_train,y_train,epochs=100,batch_size=32) ###training is done

        ####save model
        if os.path.isfile('models/%s_model.h5'%name) is False:
            model.save('models/%s_model.h5'%name)

        test_pred = model.predict(X_test)
        train_pred = model.predict(X_train)
        #print("train_pred",train_pred.shape,len(train_pred))
        #print("test_pred",test_pred.shape)

        test_pred = scaler.inverse_transform(test_pred)
        train_pred =scaler.inverse_transform(train_pred)
        y_test = y_test.reshape(y_test.shape[0], 1)
        y_test = scaler.inverse_transform(y_test)

        test_pred = test_pred.reshape(test_pred.shape[0])
        train_pred = train_pred.reshape(train_pred.shape[0])


        ###visualising the results
        trainPredictPlot = [None]*len(dataframe_avg_price['avg_price'])
        trainPredictPlot[60:len(train_pred)+60] = train_pred
        testPredictPlot = [None]*len(dataframe_avg_price['avg_price'])
        testPredictPlot[len(train_pred)+60+1:] = test_pred

        fig = plt.figure(figsize=(12,6))
        plt.plot(dataframe_avg_price['avg_price'],color = 'blue',label = 'original price')
        plt.plot(trainPredictPlot,color= 'green',label = 'train_predict')
        plt.plot(testPredictPlot,color = 'red',label='test_predict')


        plt.title('Vorhersage von durchschnitlicher Preisentwicklung (%s)'%name)
        plt.xlabel('Zeit')
        plt.ylabel('durchschnittliche Preise (€)')
        plt.legend()
        #fig.savefig('image/Predict_%s.svg'%name)
        plt.show()