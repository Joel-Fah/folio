document.addEventListener('DOMContentLoaded',function(event){
    // array with texts to type in typewriter
    var dataTextHTML = document.getElementById('demo').getAttribute('data-typed-items'); // [ "Utrecht.", "Full Service.", "Webdevelopment.", "Wij zijn Codefield!"];
    var initialArray = dataTextHTML.split('|')

    // Shuffle the array in a random order
    for (var i = initialArray.length - 1; i > 0; i--) {
        var j = Math.floor(Math.random() * (i + 1));
        [initialArray[i], initialArray[j]] = [initialArray[j], initialArray[i]];
    }

    // Join the array back into a string with "|" as the separator
    var shuffledString = initialArray.join("|");

    // Split the shuffled string again into an array using "|"
    var dataText = shuffledString.split("|");
    
    // type one text in the typwriter
    // keeps calling itself until the text is finished
    function typeWriter(text, i, fnCallback) {
      // chekc if text isn't finished yet
      if (i < (text.length)) {
        // add next character to h1
       document.querySelector("#demo").innerHTML = text.substring(0, i+1) +'<span id="carret" aria-hidden="true"></span>';
  
        // wait for a while and call this function again for next character
        setTimeout(function() {
          typeWriter(text, i + 1, fnCallback)
        }, 100);
      }

      // text finished, call callback if there is a callback function
      else if (typeof fnCallback == 'function') {
        // call callback after timeout
        setTimeout(fnCallback, 10000);
      }
    }
    // start a typewriter animation for a text in the dataText array
     function StartTextAnimation(i) {
       if (typeof dataText[i] == 'undefined'){
          setTimeout(function() {
            StartTextAnimation(0);
          }, 10000);
       }
       // check if dataText[i] exists
      if (i < dataText[i].length) {
        // text exists! start typewriter animation
       typeWriter(dataText[i], 0, function(){
         // after callback (and whole text has been animated), start next text
         StartTextAnimation(i + 1);
       });
      }
    }
    // start the text animation
    StartTextAnimation(0);
  });