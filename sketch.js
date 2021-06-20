

let fps = 15;

let direction;

let startingXPosition = 100;
let segments = 3;

let xCoordinate = []

function setup() {
  createCanvas(400, 400);
  frameRate(fps);

  for (var index = 0; index < segments; index++) {
      xCoordinate.push(index);
      
      rect(startingXPosition[index-25], height/2, 25, 25);
  }
}

function draw() {
  background(26);

  translate(-15, -15)
  
  fill(255);
  strokeWeight(1);
  
  // for (var index = 0; index < x)
  rect(50, 50, 25, 25);
  // rect(startingXPosition-25, height/2, 25, 25);
  // rect(startingXPosition, height/2, 25, 25);
  // rect(startingXPosition-25, height/2, 25, 25);

  startingXPosition++;
}

function keyPressed() {
  switch (keyCode) {
    case LEFT_ARROW:
      if (direction !== 'RIGHT') {
        direction = 'LEFT';
      }
      break;
    case RIGHT_ARROW:
      if (direction !== 'LEFT') {
        direction = 'RIGHT';
      }
      break;
    case UP_ARROW:
      if (direction !== 'DOWN') {
      direction = 'UP';
      }
      break;
    case DOWN_ARROW:
      if (direction !== 'UP') {  
        direction = 'DOWN';
      }
      break;
  }
}
