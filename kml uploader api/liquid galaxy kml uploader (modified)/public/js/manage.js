"use strict";
$(document).ready(function() {

  var displayKmlList = function () {
    var curl = "http://localhost:5430/kml/manage/current";
    fetch(curl).then(function(response) {
        if(response.ok) {
            response.json().then(function(data) {
                var curr = data;
                var url = "http://localhost:5430/kml/manage/";
                fetch(url, {
                  method: 'PUT',
                })
                  .then(function(response) {
                      if(response.ok) {
                        response.json().then(function(data) {
                          var kmls = document.getElementById('kmls');
                          while (kmls.childNodes.length > 2) {
                              kmls.removeChild(kmls.lastChild);
                          }
                          for (var i = 0; i < data.length; i++) {
                            var li = document.createElement("li");
                            var content = document.createElement("div");
                            var header = document.createElement("button");
                            var delbutton = document.createElement("button");
                            var setbutton = document.createElement("button");
                            var p = document.createElement("p");
                            var kmel = document.createTextNode(data[i].name);
                            var kminfo = document.createTextNode("Path: " + data[i].path);
                            var deltext = document.createTextNode("Delete KML");
                            var settext = document.createTextNode("Set as Current");

                            var att = document.createAttribute("class");
                            att.value = "collapsible";
                            header.setAttributeNode(att);
                            var att2 = document.createAttribute("class");
                            att2.value = "content";
                            content.setAttributeNode(att2);
                            var att3 = document.createAttribute("width");
                            att3.value = "100%";
                            p.setAttributeNode(att3);
                            var att4 = document.createAttribute("id");
                            att4.value = i;
                            delbutton.setAttributeNode(att4);
                            var att5 = document.createAttribute("id");
                            att5.value = i;
                            setbutton.setAttributeNode(att5);
                            var att6 = document.createAttribute("class");
                            att6.value = "small";
                            delbutton.setAttributeNode(att6);
                            var att7 = document.createAttribute("class");
                            att7.value = "small";
                            setbutton.setAttributeNode(att7);
                            if (i == curr.current.id) {
                              var att8 = document.createAttribute("class");
                              att8.value = "collapsible current";
                              header.setAttributeNode(att8);
                            }

                            header.addEventListener("click", function() {
                              this.classList.toggle("active");
                              var content = this.nextElementSibling;
                              if (content.style.display === "block") {
                                content.style.display = "none";
                              } else {
                                content.style.display = "block";
                              }
                            });
                            //console.log(i)
                            delbutton.addEventListener("click", function(e) {
                              var url = "http://localhost:5430/kml/manage/" + e.target.id;
                              fetch(url, {
                                method: 'DELETE',
                                headers: {
                                  'Content-Type': 'application/json'
                                },
                              }).then(function(response) {
                                  if(response.ok) {
                                    response.json().then(function(data) {
                                      console.log(data);
                                      displayKmlList();
                                    });
                                  } else {
                                      console.log("response failed");
                                  }
                              });
                            });
                            setbutton.addEventListener("click", function(e) {
                              var url = "http://localhost:5430/kml/manage/" + e.target.id;
                              fetch(url, {
                                method: 'PUT',
                              }).then(function(response) {
                                  if(response.ok) {
                                    response.json().then(function(data) {
                                      console.log(data);
                                      displayKmlList();
                                    });
                                  } else {
                                      console.log("response failed");
                                  }
                              });
                            });

                            header.appendChild(kmel);
                            li.appendChild(header);
                            p.appendChild(kminfo);
                            content.appendChild(p);
                            delbutton.appendChild(deltext);
                            content.appendChild(delbutton);
                            setbutton.appendChild(settext);
                            content.appendChild(setbutton);
                            li.appendChild(content);
                            kmls.appendChild(li);
                          }
                        });
                      } else {
                          console.log("response failed");
                      }
                  });
            })
        }
        else {
            console.log("fail")
        }
    });
  };

  var add = $('#crud');
  add.click(function() {
    this.classList.toggle("active");
    var content = this.nextElementSibling;
    if (content.style.display === "block") {
      content.style.display = "none";
    } else {
      content.style.display = "block";
    }
  });

  var namesub = $('#namesub');
  namesub.click(function() {
    var url = "http://localhost:5430/kml/manage/new?name=" + $('#name').val();
    fetch(url, {
      method: 'POST',
    }).then(function(response) {
        if(response.ok) {
          response.json().then(function(data) {
            console.log(data);
            displayKmlList();
            location.reload();
          });
        } else {
            console.log("response failed");
        }
    });
  });

  displayKmlList();

}); // end ready()
