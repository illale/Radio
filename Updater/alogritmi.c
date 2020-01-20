float averages[6]
char payload[]
float result[6];

accle = list[i][k] - calibration_value
velocity.append(velocity[i - 1] + accle)
position.append(position[i - 1] + velocity[i - 1])



void calc_position() {
  int i, k;
  float acceleration;
  for (k = 0; k < 3; k++) {
    for (i = 1; i < 20; i++) {
      acceleration = MPU_Data[i][k];
    }
  }
}


if ((averages[3] < -20 && averages[4] < -20 && averages[5] > 20) || (averages[3] > 5 && averages[4] < -10 && averages[5] > 10)) {
  if (position[0] < -30 && position[1] < -20 && (position[2] < -20 || position[2] > 20) ) {
    myState = SEND_MESSAGE;
    payload = "Ylavitonen";
  }
} else if ((averages[4] < -20 && averages[5] > 20 && averages[6] > 20) || (averages[4] > 10 && (-5 < averages[5] || averages[5] < 5) && averages[6] > 20)) {
  if (position[0] > 40 && position[1] > 40 && position[2] < -40) {
    myState = SEND_MESSAGE;
    payload = "Alavitonen";
  } else if (position[0] < -40 && position[1] < -40 && position[2] < 0) {
    myState = SEND_MESSAGE;
    payload = "Alavitonen";
  }
}
