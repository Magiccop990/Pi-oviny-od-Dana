function OnClick() {
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;
    var button = document.getElementById("button");
    alert("You Signed In as: " + username + " with password: " + password);
    window.location = "index2SI.html"
}