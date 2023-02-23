<!DOCTYPE html>
<html lang="en">
 <head>
  <meta charset="utf-8" />
  <title>Autochat</title>
 </head>
 <body>
  <script src="autoChat.js"></script>
  <h1 style="text-align:center">Autochat: an easy access to chatgpt</h1>
  <h4 style="text-align:center">Made by Wendy</h4>
  <form name = "wrap" id="wrap" target="form1" action="#" method="post" onsubmit="chat()">
    Please input your text:<br>
    <textarea id="content" rows="5" name="content" maxlength="1000" cols="100" placeholder="Say hello world!"></textarea>
    <br><br>
    <input type="submit" value="Send to chatgpt">
  </form>
  <p id="res"></p>
  <iframe name="form1" id="form1" style="display:none"></iframe>
</body>
</html>