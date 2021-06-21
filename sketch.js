

let fps = 15;

let direction;

let startingXPosition = 400;
let segments = 3;

let xCoordinate = []

function setup() {
  createCanvas(400, 400);
  frameRate(fps);
}

function draw() {
  background(26);

  translate(-15, -15)
  
  fill(255);
  strokeWeight(1);
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
