package com.headmetal.headwareintelligence

import androidx.compose.foundation.Image
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.res.painterResource
import androidx.compose.ui.text.font.FontWeight
import androidx.navigation.NavController
import kotlinx.coroutines.delay

@Preview(showBackground = true)
@Composable
fun Loading(navController: NavController, modifier: Modifier = Modifier) {
    LaunchedEffect(key1 = true) {
        delay(3000)
        navController.navigate("loginScreen")
    }
    Surface(
        modifier = modifier,
        color = Color(0xFFF9C94C)
    ) {
        Column(
            verticalArrangement = Arrangement.Center,
            horizontalAlignment = Alignment.CenterHorizontally
        ) {
            Image(
                painter = painterResource(id = R.drawable.helmet),
                contentDescription = null
            )
            Text(
                text = "HeadWear - Intelligence",
                fontWeight = FontWeight.Bold
            )
        }
    }
<<<<<<< HEAD
}
=======
}
>>>>>>> 8cdd76ccc95ba9155dd155f1510737d641e2f259
