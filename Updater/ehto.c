
if (-0.6 < Variances[0] < -0.3) {
    if (-0.1 < Variances[1] < 0.1) {
    // X-Yla
    System_printf("Alavitonen");
    System_flush();
  } else if (-0.5 < Variances[1] < -0.3) {
    // Y-Yla
    System_printf("Alavitonen");
    System_flush();

  } else if (-0.9 < Variances[1] < -0.6) {
    // X-Ala
    System_printf("Alavitonen");
    System_flush();

  } else if (0.1 < Variances[1] < 0.3) {
    // Y-Ala
    System_printf("Alavitonen");
    System_flush();
  }
    myState = SEND_MESSAGE;
} else {
    myState = READ_MESSAGE;
}
