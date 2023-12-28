var cards = [
    "assessment/death13.jpeg",
    "assessment/hierophant.jpeg",
    "assessment/silver_chariot.jpeg",
    "assessment/star_platinum.jpeg",
    "assessment/theworld.jpeg"
  ];
  
  for (var i = 0; i < 5; i++) {
    var img = document.createElement("img");
    img.src = cards[i];
    img.style.display = 'none';
    var button = document.createElement('button');
    button.setAttribute('data-index', i); 
    button.style.backgroundImage = 'url(assessment/backside.jpeg)';
    button.style.width = '200px';
    button.style.height = '200px';
    button.style.backgroundSize = 'cover';
  
    button.addEventListener('click', function(e) {
      var index = e.target.getAttribute('data-index');
      var clickedImg = document.querySelector("img[src='" + cards[index] + "']"); 
      clickedImg.style.display = 'block';
    });
  
    document.body.appendChild(button);
    document.body.appendChild(img);
  }

  for (var i = 0; i < 5; i++) {
    var img = document.createElement("img");
    img.src = cards[i];
    img.style.display = 'none';
    var button = document.createElement('button');
    button.setAttribute('data-index', i); 
    button.style.backgroundImage = 'url(assessment/backside.jpeg)';
    button.style.width = '200px';
    button.style.height = '200px';
    button.style.backgroundSize = 'cover';
  
    button.addEventListener('click', function(e) {
      var index = e.target.getAttribute('data-index');
      var clickedImg = document.querySelector("img[src='" + cards[index] + "']"); 
      clickedImg.style.display = 'block';
    });
  
    document.body.appendChild(button);
    document.body.appendChild(img);
  }