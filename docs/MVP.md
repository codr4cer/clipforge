# ClipForge — MVP v0.1

## Objectif

Créer un outil local capable de transformer une vidéo YouTube longue en une liste d’extraits courts à fort potentiel pour TikTok, Instagram Reels et YouTube Shorts.

## Fonctionnalités v0.1

- Télécharger une vidéo YouTube à partir d’une URL.
- Transcrire automatiquement la vidéo avec Whisper.
- Sauvegarder la transcription en `.txt`, `.srt` et `.json`.
- Analyser la transcription pour identifier les meilleurs passages.
- Retourner une liste structurée de clips potentiels avec :
  - timecode de début ;
  - timecode de fin ;
  - score de potentiel viral ;
  - accroche proposée ;
  - raison du choix.

## Hors périmètre v0.1

- Interface graphique.
- Publication automatique.
- Sous-titres stylisés.
- Recadrage intelligent.
- Export automatique des clips finaux.

## Pipeline v0.1

URL YouTube
→ Téléchargement
→ Transcription
→ Analyse IA
→ Liste des meilleurs extraits

## Modules

### downloader

Responsable du téléchargement vidéo.

Entrée :
- URL YouTube

Sortie :
- chemin du fichier vidéo téléchargé

### transcriber

Responsable de la transcription.

Entrée :
- chemin du fichier vidéo

Sortie :
- fichiers de transcription `.txt`, `.srt`, `.json`

### analyzer

Responsable de l’analyse IA.

Entrée :
- transcription texte

Sortie :
- liste JSON des meilleurs extraits

### exporter

Responsable de l’organisation des résultats.

Entrée :
- résultats de l’analyse

Sortie :
- fichier `clips_suggestions.json`

## Critères de réussite

Le MVP est réussi si, pour une vidéo YouTube donnée, le logiciel produit automatiquement un fichier contenant une liste d’extraits potentiels prêts à être découpés.