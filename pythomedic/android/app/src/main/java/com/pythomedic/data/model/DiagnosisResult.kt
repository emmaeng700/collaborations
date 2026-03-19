package com.pythomedic.data.model

// TODO (Acheampong): Data class matching /diagnose API response
// DEPENDS ON: Oppong → finalize diagnose.py response schema
data class DiagnosisResult(
    val disease: String = "",
    val confidence: Float = 0f,
    val advice: String = "",
    val timestamp: Long = 0L
)
