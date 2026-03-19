package com.pythomedic.data.model

// TODO (Acheampong): Data class for MQTT spray commands sent to robot
// DEPENDS ON: Akontoke → MQTT topic names in robot_broker.py
data class SprayCommand(
    val action: String = "",   // "spray" | "stop"
    val duration: Int = 0      // seconds
)
