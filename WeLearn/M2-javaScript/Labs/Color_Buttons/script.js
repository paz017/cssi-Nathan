// Copyright 2018 Google LLC
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

// Use querySelector to store the div in a variable.
const redButton = document.querySelector('#red');
let repeatText = ''

// Use addEventListener to respond to a click event.
redButton.addEventListener('click', (e) => {
  console.log("You clicked the red button!");

  let responseBox = document.querySelector("#response-box")

  responseBox.style.backgroundColor="red";
  repeatText = repeatText + "red ";
  responseBox.innerHTML = repeatText;
});

//----------------------------------------------------

const greenButton = document.querySelector('#green');

// Use addEventListener to respond to a click event.
greenButton.addEventListener('click', (e) => {
  console.log("You clicked the green button!");

  let responseBox = document.querySelector("#response-box")

  responseBox.style.backgroundColor="green";
  repeatText = repeatText + "green ";
  responseBox.innerHTML = repeatText;
});

//----------------------------------------------------

const blueButton = document.querySelector('#blue');

// Use addEventListener to respond to a click event.
blueButton.addEventListener('click', (e) => {
  console.log("You clicked the blue button!");

  let responseBox = document.querySelector("#response-box")

  responseBox.style.backgroundColor="blue";

  repeatText = repeatText + "blue ";
  responseBox.innerHTML = repeatText;
});

//----------------------------------------------------
