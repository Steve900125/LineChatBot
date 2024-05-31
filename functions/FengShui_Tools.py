import re

def get_fengshui_advice( problem ):
    fenshui_advice = {
        '對門煞' : "以前人覺得門與門相對，會擾亂氣流，造成心煩意亂，因此容易發生衝突。嚴重的話，甚至會導致家庭失和，進而破財，或發生血光之災。若以較為科學的角度來看，兩門正對的確會引起較大的對流。若門沒有緩衝，可能會被大力關上，讓人嚇一跳，或是誤以為對方大聲關門。長期下來，會導致心神不寧、居者感情不和諧。"
        , '壓樑' : "傳統風水認為，橫梁猶如一把刀，若是懸在常坐的沙發或是床上，就如同懸掛著危險，輕則損及健康，容易造成腦神經衰弱、頭痛，重則危及生命。"
        , '陽宅內六室':"內六事，包括了門、灶、路、井、厕、錐磨"
    }
    problem = re.sub(r'[^\u4e00-\u9fff]', '', problem)
    print("'{0}'風水建議資料搜尋中 .....".format(problem))

    if problem in fenshui_advice:
        return fenshui_advice[problem] 
    else :
        return "目前沒有相關資料，搜尋網路上資料來做回覆"
