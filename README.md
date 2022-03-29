## Routes API

### Page d'accueil de l'API
**GET** `/api/v1` 
#### 200
```json
{
	"authors": [
		{
			"github": "https://github.com/TheoBIET",
			"name": "Théo BIET"
		},
		{
			"github": "https://github.com/EricClouzet",
			"name": "Éric Clouzet"
		},
		{
			"github": "https://github.com/mm-devpro",
			"name": "Mickael Milliat"
		},
		{
			"github": "https://github.com/Worcesters",
			"name": "Jérémy"
		}
	],
	"message": "Welcome to the Remake IT API!",
	"version": "0.1.0"
}
```

#### Upload d'une image
**POST** `/api/v1/upload`
#### 400 - Aucun fichier n'a été envoyé
```json
{
	"error": true,
	"message": {
		"en": "No file has been sent.",
		"fr": "Aucun fichier n'a été envoyé."
	}
}
```
#### 400 - Mauvais format de fichier
```json
{
	"allowed_extensions": [
		"jpg",
		"jpeg",
		"gif",
		"png",
		"webp"
	],
	"error": true,
	"file": "MacroBOT.kmmacros",
	"message": {
		"en": "The file is not allowed",
		"fr": "Le fichier n'est pas autorisé"
	}
}
```
#### 200
```json
{
	"error": false,
	"file": "unknown.PNG",
	"message": {
		"en": "File sent successfully!",
		"fr": "Fichier envoyé avec succès!"
	}
}
```
