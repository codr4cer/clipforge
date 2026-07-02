# ClipForge — Viral Engine v0.2

## Objectif

Identifier automatiquement les passages d'une vidéo longue qui ont le plus fort potentiel pour devenir des shorts performants.

## Définition d'un bon extrait

Un bon extrait doit :

- capter l'attention en moins de 3 secondes ;
- être compréhensible sans contexte long ;
- créer de la curiosité ;
- provoquer une émotion ou une réaction ;
- contenir une idée claire ;
- durer idéalement entre 20 et 60 secondes ;
- donner envie de commenter, partager ou regarder jusqu'au bout.

## Critères de scoring

Chaque extrait potentiel sera noté sur 100.

### 1. Hook / accroche — 25 pts

Le passage contient-il une phrase forte dès le début ?

### 2. Curiosité — 20 pts

Le passage donne-t-il envie de connaître la suite ?

### 3. Valeur — 15 pts

Le spectateur apprend-il quelque chose d'utile ou intéressant ?

### 4. Émotion — 15 pts

Le passage provoque-t-il surprise, rire, tension, admiration, indignation ou nostalgie ?

### 5. Clarté — 10 pts

Le passage est-il compréhensible sans avoir vu toute la vidéo ?

### 6. Commentaires — 10 pts

Le passage peut-il déclencher un débat ou une réaction ?

### 7. Longueur — 5 pts

Le passage est-il exploitable en format short ?

## Format JSON attendu

```json
{
  "clips": [
    {
      "id": 1,
      "start": "00:02:15",
      "end": "00:02:58",
      "duration_seconds": 43,
      "score": 87,
      "hook": "Cette voiture cache un défaut énorme...",
      "reason": "Le passage combine curiosité, opinion forte et sujet automobile clivant.",
      "title": "Le défaut caché de cette voiture",
      "hashtags": ["automobile", "voiture", "mecanique", "cartok"]
    }
  ]
}