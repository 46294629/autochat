function chat()
{
    var xhr = new XMLHttpRequest();
    var url = "http://{IP}:{PORT}"
    xhr.open('POST', url, true); 
    xhr.setRequestHeader("Content-type","application/json");
    var data = document.getElementById("content").value
    console.log(data);
    document.getElementById("res").innerHTML = "sending..."
    xhr.send(JSON.stringify(data));
    xhr.onreadystatechange = function () {
    console.log(xhr.status)
    if (xhr.status == 200) {
        var json = eval(xhr.responseText);
        console.log(json);
        document.getElementById("res").innerHTML = json;
    }}
} 