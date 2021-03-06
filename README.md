# 2018-104Hackathon-Chatbot

隨著 AI 技術以及語意分析技術的發展，對話式商務快速崛起，請參賽者利用主辦單位提供之資料集打造 Chatbot，回答主辦單位指定的問題。

## 活動網址
https://www.104.com.tw/hackathon/2018/

## 主題說明
主辦單位將提供包含是非題、選擇題、填空題等 3 種題型，每種題型難易度不同，答對得分也不同，參賽 Slack Chatbot 需於規定時間內答題獲取積分，主辦單位將會依照參賽隊伍獲得的積分作為評分標準。

## 聊天平台說明
此次比賽將使用 Slack 聊天平台，每場賽事會有專屬 Channel，參賽 Chatbot 需於該 Channel 上接收與回答問題！

### 加入 104Hackathon Chatbot Slack Team 步驟說明
* 主辦單位會發送 Slack 邀請函至參賽者報名 email，請參賽者收到邀請函後隨即加入 104Hackathon Chatbot Team
* 主辦單位會幫所有報名隊伍建立 Chatbot，並將 Token 寄送至參賽者 email，請參賽者收到後妥善保管，切勿外流
* 各隊的 Chatbot 會被自動加到測試頻道，主辦單位會不定時在測試頻道上貼出測試題供參賽 Chatbot 進行測試

### 範例
主辦單位將會提供 SlackBot 程式範例，參賽者可參考範例撰寫比賽程式！
* [SlackBot 程式範例](https://github.com/104corp/2018-104Hackathon-Chatbot/tree/master/sample-code)

### Reference:
* https://github.com/slackapi/python-slackclient

## 資料集說明
* 公司資料
    + 企業基本資料
        - File: company.json
        - Decription: 資料集中所使用的公司資料
        - [Company Schema](data-schema/companies_schema.md)
        - [Company Sample](sample-data/companies_sample.json)
        - [資料集下載連結](2018-104-hackathon-dataset.md)
* 勞基法相關法條資料: 
    + 此資料集出處為[全國法規資料庫](https://law.moj.gov.tw/Index.aspx)，使用前請先閱讀、瞭解並同意其[開放資料宣告](https://law.moj.gov.tw/Service/Copyright.aspx)。
    + [下載連結](https://www.104.com.tw/hackathon/2018/dataset/labor-standards-act.html) 

## 規則說明與範例

本次賽事包含積分賽與決賽, 說明如下：

### 積分賽
* 說明
	- 官方Chatbot 每 N 秒會在頻道貼出題目
	- 參賽Chatbot 需將答案以 ephemeral message 的方式傳給官方Chatbot
    - 只接受每位參賽Chatbot 的第一個答案
    - 每題可獲得的積分依題目難度不同
* 範例
    * 是非題
        - 參賽Chatbot 會收到以下訊息內容
            ```
            Id: 1
            Type: 是非題
            From: 104人力銀行_一零四資訊科技股份有限公司 - 公司簡介
            Score: 2
            Question: 
            以下描述是否正確?
            104的誕生，緣於失業的社會問題。我們肩上，一直有一份社會責任，一種想安定職場的力量，想關愛土地的活力。
            ```
        - 參賽Chatbot 需回答以下內容:
            ```
            Id: 1
            Answer: O
            ```
        - 答案為是請回答大寫"O", 為非請回答大寫 "X"
        - 其中 From 有可能為空
    * 選擇題
        - 參賽Chatbot 會收到以下訊息內容
            ```
            Id: 1
            Type: 選擇題
            From: 104人力銀行_一零四資訊科技股份有限公司 - 公司簡介
            Score: 3
            Question: 
            以下____為何? 
            104的誕生，緣於失業的社會問題。我們肩上，一直有一份社會責任，一種想安定職場的力量，想關愛____的活力。
            選項:
            (1) 森林
            (2) 山脈
            (3) 土地
            (4) 大海
            ```
        - 參賽Chatbot 需回答以下內容:
            ```
            Id: 1
            Answer: 3
            ```
        - 其中 From 有可能為空
    * 填空題
        - 參賽Chatbot 會收到以下訊息內容
            ```
            Id: 1
            Type: 填空題
            From: 104人力銀行_一零四資訊科技股份有限公司 - 公司簡介
            Score: 3
            Length: 2
            Question: 
            104的誕生，緣於____的社會問題。我們肩上，一直有一份社會責任，一種想安定職場的力量，想關愛土地的活力。
            ```
        - 參賽Chatbot 需回答以下內容:
            ```
            Id: 1
            Answer: 失業
            ```
        - 其中 From, Length 有可能為空

### 決賽
* 說明
	- 取積分賽前 5 名進入決賽
	- 官方Chatbot 每 10 秒會在頻道貼出題目
	- 參賽Chatbot 需在頻道上貼出答案
	- 第一個答對者得分
	- 每題可獲得的積分依題目難度不同
    - 題目有可能為是非題, 選擇題或填空題
* 答題方式
    - 官方Chatbot 會隨機詢問是非題、選擇題、填空題三種類型的題目
    - 參賽Chatbot 接收到的題目格式與需送出的答案格式與積分賽一致
    - 不同於積分賽答案以 ephemeral message 的方式傳給官方Chatbot，決賽時需直接將答案貼到比賽頻道

## 題目

### 題目出處
題目主要來自勞基法相關法條與104公司資料庫:
* 勞基法相關
    - 勞動基準法
    - 勞動檢查法
    - 就業保險法
    - 就業服務法
    - 勞工保險條例
    - 勞工退休金條例
    - 勞資爭議處理法
    - 性別工作平等法
    - 勞動基準法施行細則
* 104公司資料庫
	- 公司簡介(profile)
	- 主要商品/服務項目(product)
	- 福利制度(welfare)
    - 經營理念(management)

### 變化
題目會對原文做一些基本的變化，包括
* 一字不刪
    - 會使用與原文一模一樣的文字內容
* 稍做變化
	- 刪除原文中的某些字詞或符號
* 前後文對調
    - 將原文的字詞或句子不做修改，但往前搬移或往後移動
* 換句話說
    - 將原文以不同的字詞或句子進行重整

### 資訊
出題時會依難易度提供以下資訊
* 提供答案總共有幾個字
* 提供題目出處
	- 針對勞基法相關，會提供題目出自哪個法律的第幾條
	- 針對公司資訊，會提供出自哪間公司的哪個欄位

### 題目範例
* [是非題](sample-question/是非題.csv)
* [選擇題](sample-question/選擇題.csv)
* [填空題](sample-question/填空題.csv)
* [決賽題](sample-question/決賽題.csv)

### 影片範例
* [是非題](sample-video/是非題.mp4)
* [選擇題](sample-video/選擇題.mp4)
* [填空題](sample-video/填空題.mp4)
* [決賽題](sample-video/決賽題.mp4)

## 評分標準
* 積分結果 70%
* 設計方法 30%（包含簡報內容、演算法設計、資料闡釋與分析等）
* 分數計算方式
    - 三場積分賽：當天會針對是非題、選擇題、填空題個別舉辦積分賽，取總分前 5 名進入決賽
    - 決賽：各隊決賽所獲分數 * 0.7 + 設計方法分數

附註: 主辦單位保留規則微調之權利

## 104開放資料授權條款 
【2018-104-hackathon-dataset】是 2018年104資訊科技Hackathon活動中開放的資料集。當您使用104提供之【2018-104-hackathon-dataset】資料集時，即表示您已閱讀、瞭解並同意接受本授權條款所訂定之所有內容。本授權條款得隨時修訂並公告於本頁面上，修訂後之內容自公告時起生效，授權說明如下：

* 使用者權利：
    + 使用者得自由應用104提供的資料集，產生新的程式、文件、圖表等著作，使用者亦可自由修改104提供的資料集，衍生新的資料集，使用者基於本活動目的範圍的任何使用方式，無須104再為授權。
* 使用者義務：
    + 使用者必須在您的著作或衍生資料集明確標示【2018年104資訊科技Hackathon】為資料來源，與此份說明文件的連結。
    + 使用者違反前項標示義務，視為自始未取得104開放資料之授權，須負擔所有相關之法律責任。
* 使用者規範：
    1. 使用者不可使用可能造成104會員混淆或困擾的商標或名稱，或為任何違反104會員服務條款或本活動授權規範之行為。
    2. 使用者不可違反中華民國法令，或造成第三人發生違反中華民國法令的行為。
    3. 使用者保證不可另為提供他人資料集下載，意即，使用者不得複製一份資料集到您自己的網路服務上供他人下載，但您可以提供他人此份說明文件的連結。使用者同意且了解，若您利用104提供的資料集，開發任何妨礙善良風俗之違法服務或程式工具，104並不為此負擔任何法律連帶責任。
    4. 使用者不得意圖或為任何可能損害104商譽或侵害104資料之任何行為或聲明。
    5. 謝絕競業使用，作任何商業營利或非商業研究分析之用。
    6. 本條款之解釋、效力、履行及其他未盡事宜，以中華民國法律為準據法。

