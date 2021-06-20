

let fps = 20;

function setup() {
  createCanvas(400, 400);
  frameRate(fps);
}
let direction;

function draw() {
  background(225);

  translate(-15, -15)
  fill(26);
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
