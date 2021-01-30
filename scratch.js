
// document.head.setAttribute('src', 'http://ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js');
// const papa_script = jQuery.createElement('script');
// papa_script.setAttribute('src', 'https://cdnjs.cloudflare.com/ajax/libs/PapaParse/5.3.0/papaparse.min.js');
// document.head.appendChild(papa_script);

// var reader = FileReader();
// reader.readAsText('./iris.csv');
// console.log(reader.result);

var dict = {'a': 'apple', 'b': 'banana', 'c' : 'cherry', 'd': 1.23};
var first = dict[0];
console.log(first);
delete dict[first];
console.log(dict);
console.log(first);
