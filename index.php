<?php

function getPaysInfo($url) {
    // Initialise une ressource cURL
    $curl = curl_init();

    // Définit l'URL à partir de laquelle récupérer les données
    curl_setopt($curl, CURLOPT_URL, $url);

    // Définit l'option pour retourner le résultat de la requête au lieu de l'afficher
    curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);

    // Exécute la requête cURL et récupère les données
    $payData = curl_exec($curl);

    // Vérifie s'il y a eu une erreur lors de la requête
    if(!$payData) {
        // En cas d'erreur, affiche un message d'erreur
        echo 'Erreur : ' . curl_error($curl);
    }

    // Ferme la ressource cURL
    curl_close($curl);

    // Décode les données JSON en un tableau associatif
    $paysArray = json_decode($payData, true);

    // Initialise un tableau pour stocker les informations des pays
    $paysInfo = array();

    // Parcours le tableau associatif pour extraire les informations des pays
    foreach ($paysArray as $pays) {
        // Crée un tableau associatif avec le nom et le lien du drapeau pour chaque pays
        $info = array(
            'name' => $pays['name'],
            'flag' => $pays['flags']['png'],
            'population' => $pays['population'],
            'lat' => $pays['latlng'][0]?? null,
            'lon' => $pays['latlng'][1]?? null,
            'weather' => getWeatherInfo($pays['name']) // Appel de la fonction pour obtenir les informations météorologiques
        );

        // Ajoute les informations du pays au tableau des informations
        $paysInfo[] = $info;
    }

    // Retourne le tableau des informations des pays
    return $paysInfo;
}

function getWeatherInfo($city) {
    // Remplacez 'YOUR_API_KEY' par votre propre clé API OpenWeatherMap
    $apiKey = '29f83a1cf93485288601b303e6748b89';
    // URL de l'API OpenWeatherMap pour obtenir les informations météorologiques actuelles par ville
    $url = `http://api.weatherstack.com/current?access_key=${apiKey}&query=${city}`;
    
    // Initialise une ressource cURL
    $curl = curl_init();

    // Définit l'URL à partir de laquelle récupérer les données
    curl_setopt($curl, CURLOPT_URL, $url);

    // Définit l'option pour retourner le résultat de la requête au lieu de l'afficher
    curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);

    // Exécute la requête cURL et récupère les données
    $weatherData = curl_exec($curl);

    // Vérifie s'il y a eu une erreur lors de la requête
    if(!$weatherData) {
        // En cas d'erreur, affiche un message d'erreur
        echo 'Erreur : ' . curl_error($curl);
    }

    // Ferme la ressource cURL
    curl_close($curl);

    // Décode les données JSON en un tableau associatif
    $weatherArray = json_decode($weatherData, true);

    // Retourne les informations météorologiques
    return $weatherArray;
}

// Exemple d'utilisation de la fonction avec un lien distant
$paysInfo = getPaysInfo('https://restcountries.com/v2/all');

// Affiche les informations des pays récupérées
foreach ($paysInfo as $pays) {
    echo 'Nom : ' . $pays['name'] . "<br>";
    echo 'Population : ' . $pays['population'] . '<br>';
    echo "Drapeau" . '<br>';
    echo '<img src="' . $pays['flag'] . '" alt="Drapeau de ' . $pays['name'] . '">' . "<br>";
    echo "<br>";
    echo 'Longitude : ' . $pays['lon'] . '<br>';
    echo 'Latitude : ' . $pays['lat'] . '<br>';
    echo 'Météo : ' . "<br>";
    // Afficher les informations météorologiques
    if(isset($pays['weather']['main']['temp'])) {
        echo 'Température : ' . $pays['weather']['main']['temp'] . ' °C <br>';
        echo 'Humidité : ' . $pays['weather']['main']['humidity'] . ' % <br>';
        echo 'Description : ' . $pays['weather']['weather'][0]['description'] . '<br>';
    } else {
        echo 'Informations météorologiques non disponibles pour ce pays.' . '<br>';
    }
    echo '<hr>';
}

?>
