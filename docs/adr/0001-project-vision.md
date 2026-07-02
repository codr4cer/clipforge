# ADR 0001 — Project Vision

## Status

Accepted

## Context

ClipForge started as a local tool to transform long YouTube videos into short-form content suggestions.

The initial MVP focuses on:
- downloading a video;
- transcribing it;
- analyzing the transcript;
- suggesting high-potential short clips.

However, the long-term opportunity is broader than video clipping. A long-form video contains reusable ideas that can be transformed into multiple content formats.

## Decision

ClipForge will be designed as a content repurposing engine, not only as a TikTok clip generator.

The first export target will be short-form video suggestions, but the architecture must remain open to future outputs such as:

- TikTok clips;
- Instagram Reels;
- YouTube Shorts;
- LinkedIn posts;
- newsletters;
- blog articles;
- tweet/X threads;
- YouTube descriptions;
- titles and hooks.

## Architecture principle

The system must separate:

1. Content ingestion  
2. Transcription  
3. Idea extraction  
4. Viral scoring  
5. Export generation  

This separation allows ClipForge to evolve without rewriting the whole system.

## Consequences

Positive:

- The project remains scalable.
- Future features can be added cleanly.
- The core engine can be reused for multiple content formats.
- The architecture is easier to explain and maintain.

Negative:

- The initial architecture may feel heavier than a simple script.
- Development will be slower at the beginning.
- More documentation is required.

## MVP boundary

For v0.2, ClipForge will still focus only on suggesting short-form video clips.

The broader content repurposing vision is a long-term architectural direction, not an immediate feature requirement.