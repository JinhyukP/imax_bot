# imax_bot
Send a notification message via telegram when IMAX movie ticket reservation becomes available

## Make a telegram bot using "BotFather" in telegram.
In dialogue with BotFather, type

  /start
  
  /newbot
  
  (choose a name for the bot: "blah_blah_bot")
  
 Then the token is given.
 
 ## Get chat_id from the token
 1. Go to https://api.telegram.org/bot[Your_Token_BLAHBLAH1234567890]/getUpdates
 2. Send any messsage to your bot in telegram
 3. Refresh the page
 4. Now you will see the chat id

For example, the chat id is 999999999 in the following case:

{"ok":true,"result":[{"update_id":123456789,
"message":{"message_id":1,"from":{"id":999999999,"is_bot":false,"first_name"
  
  
  


# Reference
https://somjang.tistory.com/entry/Python-파이썬과-텔레그램으로-스파이더맨-노웨이홈-예매-알리미-만드는-방법 [솜씨좋은장씨]
https://gabrielkim.tistory.com/entry/Telegram-Bot-Token-%EB%B0%8F-Chat-Id-%EC%96%BB%EA%B8%B0
