class SinglelinearRegression:
    B1 = ''
    B0 = ''

    def getAverage(self, Xinput, Youtput):
        Xaverage = sum(Xinput) / len(Xinput)
        Yaverage = sum(Youtput) / len(Youtput)
        return Xaverage, Yaverage

    def Linear(self,Xinput,Youtput):
        Xmeanofx = []
        Ymeanofy = []
        Xmeansquareofx = []
        Ymeansquareofy = []
        XmeanYmeansum =[]
        ypredicted = []
        if len(Xinput) == len(Youtput):
            Xaverage, Yaverage = self.getAverage(Xinput, Youtput)
            for Xin, Yin in zip(Xinput, Youtput):
                Xmeanvalue = Xin-Xaverage
                Ymeanvalue = Yin-Yaverage
                XmeanYmeansum.append((Xin-Xaverage) * (Yin-Yaverage))
                Xmeanofx.append(Xmeanvalue)
                Ymeanofy.append(Ymeanvalue)

            for Xin, Yin in zip(Xmeanofx, Ymeanofy):
                Xmeansquareofx.append(Xin * Xin)
                Ymeansquareofy.append(Yin * Yin)
            sqrtX = sum(Xmeansquareofx)
            print(XmeanYmeansum)
            meansmultiple = sum(XmeanYmeansum)
            self.B1 = meansmultiple / sqrtX
            self.B0 = Yaverage - self.B1 * Xaverage
            for xint, predit in zip(Xinput, Youtput):
                ypredicted.append(self.B0 + self.B1 * xint)
            return ypredicted

    def RMSE(self, predictedy, Y):
        squarePredictYy = []
        LenghtofY = len(Y)
        for predictY, RealY in zip(predictedy, Y):
            Value = predictY - RealY
            squarePredictYy.append(Value * Value)
        SquarepredictY_y_Sum = sum(squarePredictYy)
        Squarerooterror = (SquarepredictY_y_Sum/LenghtofY) ** 0.5
        return Squarerooterror

    def pearsonr(self, xinput, yinput):
        SumOfx = sum(xinput)
        SumofY = sum(yinput)
        SumofXiYi = []
        Multofx = []
        Multofy = []
        for Onex , Oney in zip(xinput,yinput):
            SumofXiYi.append(Onex * Oney)
            Multofx.append(Onex * Onex)
            Multofy.append(Oney * Oney)
        Topvalue = sum(SumofXiYi) - (SumOfx*SumofY/len(xinput))
        Xvalue = (sum(Multofx) - sum(xinput)**2 / len(xinput))**0.5
        Yvalue = (sum(Multofy) - sum(yinput)**2 / len(yinput))**0.5
        Ans = (Topvalue / Xvalue) / Yvalue
        return Ans

    def Predict(self, Xnew):
        predicts = self.B0 + self.B1 * Xnew
        return predicts