

let fps = 10;

let xPosition = 100;
let yPosition = 100;
let direction = "RIGHT";
let speed = 10;

function setup() {
  createCanvas(400, 400);
  frameRate(fps);
}

let xCor = [];
let yCor = [];

function draw() {
  background(225);

  translate(-15, -15)
  fill(26);
  for (let i = 0; i < numSegments - 1; i++) {
    line(xCor[i], yCor[i], xCor[i + 1], yCor[i + 1]);
  }
  // rect(xPosition, yPosition, 30, 30);

  // switch (direction) {
  //   case "LEFT":
  //     xPosition -= speed;
  //     break;
  //   case "RIGHT":
  //     xPosition += speed;
  //     break;
  //   case "UP":
  //     yPosition -= speed;
  //     break;
  //   case "DOWN":
  //     yPosition += speed;
  //     break;
  // }
}

function keyPressed() {
  switch (keyCode) {
    case LEFT_ARROW:
      print('Left');
      direction = "LEFT";
      break;
    case RIGHT_ARROW:
      print('Right');
      direction = "RIGHT";
      break;
    case UP_ARROW:
      print('Up');
      direction = "UP";
      break;
    case DOWN_ARROW:
      print('Down');
      direction = "DOWN";
      break;
  }
}
