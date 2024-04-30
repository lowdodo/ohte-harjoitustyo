##ARCHITECTURE

#structure:

"Game follows the following architecture:"

"class diagram:"

```mermaid
classDiagram
entities <|-- repositories
sprites <|-- levels
repositories <|-- levels
levels <|-- ui
levels <--> menu
levels <--> game_loop
menu <--> game_loop


entities: Player

sprites: Child
sprites: Petal

ui:src

levels: level

repositories: PlayerRepository


```

The game has sprites for the playable, movable creatures, 1 user that can be named (not done) that plays as one of the sprites but moves multiple, a UI side with multiple different screen displays. 


