CONTEXT_DEFAULT = "*"
CONTEXT_OPERATOR = "Operator"


def _entries(messages, contexts=(CONTEXT_DEFAULT,)):
    return {
        (context, msgid): msgstr
        for context in contexts
        for msgid, msgstr in messages.items()
    }


_BASE_MESSAGES = {
    "At least one face must be selected!": "",
    "Please select edges first!": "",
    "OmniOutset Tools": "",
    "Smart Face Extrude": "",
    "Equidistant Edge Extrude": "",
    "Smart Face Extrude & Outset": "",
    "Extrude Distance": "",
    "Outward Offset": "",
    "Z Axis Offset": "",
    "OmniOutset Face | Extrude: {0:.3f} (Up/Down) | Outset: {1:.3f} (Ctrl+L/R) | [Shift] Precision | [LMB] Confirm": "",
    "OmniOutset Edge | Outset: {0:.3f} (L/R) | Z-Offset: {1:.3f} (Ctrl+Up/Down) | [Shift] Precision | [LMB] Confirm": "",
    "Smart OmniOutset Call": "",
    "OmniOutset Shortcut Configuration": "",
    "Customize the universal hotkey for Face & Edge Extrude below:": "",
    "No user keyconfig found.": "",
    "Mesh keymap not found.": "",
    "Shortcut not found. Please try restarting Blender.": "",
}


dict_hans = _entries(
    {
        "At least one face must be selected!": "\u5fc5\u987b\u9009\u4e2d\u81f3\u5c11\u4e00\u4e2a\u9762\uff01",
        "Please select edges first!": "\u8bf7\u5148\u9009\u62e9\u8fb9\uff01",
        "OmniOutset Tools": "OmniOutset \u5de5\u5177",
        "Smart Face Extrude": "\u667a\u80fd\u9762\u6324\u51fa (Face)",
        "Equidistant Edge Extrude": "\u7b49\u8ddd\u8fb9\u6324\u51fa (Edge)",
        "Smart Face Extrude & Outset": "\u667a\u80fd\u9762\u6324\u51fa\u4e0e\u5916\u6269",
        "Extrude Distance": "\u6cd5\u5411\u6324\u51fa\u8ddd\u79bb",
        "Outward Offset": "\u5916\u6269\u504f\u79fb\u8ddd\u79bb",
        "Z Axis Offset": "Z \u8f74\u5e73\u79fb",
        "OmniOutset Face | Extrude: {0:.3f} (Up/Down) | Outset: {1:.3f} (Ctrl+L/R) | [Shift] Precision | [LMB] Confirm": "OmniOutset \u9762\u6a21\u5f0f | \u6324\u51fa: {0:.3f} (\u4e0a/\u4e0b) | \u5916\u6269: {1:.3f} (Ctrl+\u5de6/\u53f3) | [Shift] \u5fae\u8c03 | [\u5de6\u952e] \u786e\u8ba4",
        "OmniOutset Edge | Outset: {0:.3f} (L/R) | Z-Offset: {1:.3f} (Ctrl+Up/Down) | [Shift] Precision | [LMB] Confirm": "OmniOutset \u8fb9\u6a21\u5f0f | \u5916\u6269: {0:.3f} (\u5de6/\u53f3) | Z \u8f74: {1:.3f} (Ctrl+\u4e0a/\u4e0b) | [Shift] \u5fae\u8c03 | [\u5de6\u952e] \u786e\u8ba4",
        "Smart OmniOutset Call": "\u667a\u80fd\u8c03\u7528 OmniOutset",
        "OmniOutset Shortcut Configuration": "OmniOutset \u5feb\u6377\u952e\u914d\u7f6e",
        "Customize the universal hotkey for Face & Edge Extrude below:": "\u8bf7\u5728\u4e0b\u65b9\u81ea\u5b9a\u4e49\u9762/\u8fb9\u6324\u51fa\u7684\u5168\u5c40\u7edf\u4e00\u5feb\u6377\u952e\uff1a",
        "No user keyconfig found.": "\u672a\u627e\u5230\u7528\u6237\u5feb\u6377\u952e\u914d\u7f6e\u3002",
        "Mesh keymap not found.": "\u672a\u627e\u5230 Mesh \u5feb\u6377\u952e\u6620\u5c04\u3002",
        "Shortcut not found. Please try restarting Blender.": "\u672a\u627e\u5230\u5feb\u6377\u952e\uff0c\u8bf7\u5c1d\u8bd5\u91cd\u542f Blender\u3002",
    },
    contexts=(CONTEXT_DEFAULT, CONTEXT_OPERATOR),
)


dict_hant = _entries(
    {
        "At least one face must be selected!": "\u5fc5\u9808\u9078\u4e2d\u81f3\u5c11\u4e00\u500b\u9762\uff01",
        "Please select edges first!": "\u8acb\u5148\u9078\u64c7\u908a\uff01",
        "OmniOutset Tools": "OmniOutset \u5de5\u5177",
        "Smart Face Extrude": "\u667a\u80fd\u9762\u64e0\u51fa (Face)",
        "Equidistant Edge Extrude": "\u7b49\u8ddd\u908a\u64e0\u51fa (Edge)",
        "Smart Face Extrude & Outset": "\u667a\u80fd\u9762\u64e0\u51fa\u8207\u5916\u64f4",
        "Extrude Distance": "\u6cd5\u5411\u64e0\u51fa\u8ddd\u96e2",
        "Outward Offset": "\u5916\u64f4\u504f\u79fb\u8ddd\u96e2",
        "Z Axis Offset": "Z \u8ef8\u5e73\u79fb",
        "OmniOutset Face | Extrude: {0:.3f} (Up/Down) | Outset: {1:.3f} (Ctrl+L/R) | [Shift] Precision | [LMB] Confirm": "OmniOutset \u9762\u6a21\u5f0f | \u64e0\u51fa: {0:.3f} (\u4e0a/\u4e0b) | \u5916\u64f4: {1:.3f} (Ctrl+\u5de6/\u53f3) | [Shift] \u5fae\u8abf | [\u5de6\u9375] \u78ba\u8a8d",
        "OmniOutset Edge | Outset: {0:.3f} (L/R) | Z-Offset: {1:.3f} (Ctrl+Up/Down) | [Shift] Precision | [LMB] Confirm": "OmniOutset \u908a\u6a21\u5f0f | \u5916\u64f4: {0:.3f} (\u5de6/\u53f3) | Z \u8ef8: {1:.3f} (Ctrl+\u4e0a/\u4e0b) | [Shift] \u5fae\u8abf | [\u5de6\u9375] \u78ba\u8a8d",
        "Smart OmniOutset Call": "\u667a\u80fd\u8abf\u7528 OmniOutset",
        "OmniOutset Shortcut Configuration": "OmniOutset \u5feb\u6377\u9375\u914d\u7f6e",
        "Customize the universal hotkey for Face & Edge Extrude below:": "\u8acb\u5728\u4e0b\u65b9\u81ea\u5b9a\u7fa9\u9762/\u908a\u64e0\u51fa\u7684\u5168\u5c40\u7d71\u4e00\u5feb\u6377\u9375\uff1a",
        "No user keyconfig found.": "\u672a\u627e\u5230\u7528\u6236\u5feb\u6377\u9375\u914d\u7f6e\u3002",
        "Mesh keymap not found.": "\u672a\u627e\u5230 Mesh \u5feb\u6377\u9375\u6620\u5c04\u3002",
        "Shortcut not found. Please try restarting Blender.": "\u672a\u627e\u5230\u5feb\u6377\u9375\uff0c\u8acb\u5617\u8a66\u91cd\u555f Blender\u3002",
    },
    contexts=(CONTEXT_DEFAULT, CONTEXT_OPERATOR),
)


dict_japanese = _entries(
    {
        "At least one face must be selected!": "\u5c11\u306a\u304f\u3068\u30821\u3064\u306e\u9762\u3092\u9078\u629e\u3059\u308b\u5fc5\u8981\u304c\u3042\u308a\u307e\u3059\uff01",
        "Please select edges first!": "\u307e\u305a\u30a8\u30c3\u30b8\u3092\u9078\u629e\u3057\u3066\u304f\u3060\u3055\u3044\uff01",
        "OmniOutset Tools": "OmniOutset \u30c4\u30fc\u30eb",
        "Smart Face Extrude": "\u30b9\u30de\u30fc\u30c8\u9762\u62bc\u3057\u51fa\u3057 (Face)",
        "Equidistant Edge Extrude": "\u7b49\u8ddd\u96e2\u30a8\u30c3\u30b8\u62bc\u3057\u51fa\u3057 (Edge)",
        "Smart Face Extrude & Outset": "\u30b9\u30de\u30fc\u30c8\u9762\u62bc\u3057\u51fa\u3057\uff06\u30a2\u30a6\u30c8\u30bb\u30c3\u30c8",
        "Extrude Distance": "\u62bc\u3057\u51fa\u3057\u8ddd\u96e2",
        "Outward Offset": "\u5916\u5074\u30aa\u30d5\u30bb\u30c3\u30c8\u8ddd\u96e2",
        "Z Axis Offset": "Z \u8ef8\u30aa\u30d5\u30bb\u30c3\u30c8",
        "OmniOutset Face | Extrude: {0:.3f} (Up/Down) | Outset: {1:.3f} (Ctrl+L/R) | [Shift] Precision | [LMB] Confirm": "OmniOutset \u9762 | \u62bc\u3057\u51fa\u3057: {0:.3f} (\u4e0a/\u4e0b) | \u30a2\u30a6\u30c8\u30bb\u30c3\u30c8: {1:.3f} (Ctrl+\u5de6/\u53f3) | [Shift] \u5fae\u8abf\u6574 | [\u5de6\u30af\u30ea\u30c3\u30af] \u78ba\u5b9a",
        "OmniOutset Edge | Outset: {0:.3f} (L/R) | Z-Offset: {1:.3f} (Ctrl+Up/Down) | [Shift] Precision | [LMB] Confirm": "OmniOutset \u30a8\u30c3\u30b8 | \u30a2\u30a6\u30c8\u30bb\u30c3\u30c8: {0:.3f} (\u5de6/\u53f3) | Z \u8ef8: {1:.3f} (Ctrl+\u4e0a/\u4e0b) | [Shift] \u5fae\u8abf\u6574 | [\u5de6\u30af\u30ea\u30c3\u30af] \u78ba\u5b9a",
        "Smart OmniOutset Call": "\u30b9\u30de\u30fc\u30c8 OmniOutset \u547c\u3073\u51fa\u3057",
        "OmniOutset Shortcut Configuration": "OmniOutset \u30b7\u30e7\u30fc\u30c8\u30ab\u30c3\u30c8\u8a2d\u5b9a",
        "Customize the universal hotkey for Face & Edge Extrude below:": "\u4ee5\u4e0b\u306e\u9762/\u30a8\u30c3\u30b8\u62bc\u3057\u51fa\u3057\u7528\u306e\u5171\u901a\u30b7\u30e7\u30fc\u30c8\u30ab\u30c3\u30c8\u3092\u30ab\u30b9\u30bf\u30de\u30a4\u30ba\uff1a",
        "No user keyconfig found.": "\u30e6\u30fc\u30b6\u30fc\u30ad\u30fc\u8a2d\u5b9a\u304c\u898b\u3064\u304b\u308a\u307e\u305b\u3093\u3002",
        "Mesh keymap not found.": "\u30e1\u30c3\u30b7\u30e5\u30ad\u30fc\u30de\u30c3\u30d7\u304c\u898b\u3064\u304b\u308a\u307e\u305b\u3093\u3002",
        "Shortcut not found. Please try restarting Blender.": "\u30b7\u30e7\u30fc\u30c8\u30ab\u30c3\u30c8\u304c\u898b\u3064\u304b\u308a\u307e\u305b\u3093\u3002Blender \u3092\u518d\u8d77\u52d5\u3057\u3066\u304f\u3060\u3055\u3044\u3002",
    },
    contexts=(CONTEXT_DEFAULT, CONTEXT_OPERATOR),
)


dict_korean = _entries(
    {
        "At least one face must be selected!": "\ud558\ub098 \uc774\uc0c1\uc758 \uba74\uc744 \uc120\ud0dd\ud574\uc57c \ud569\ub2c8\ub2e4!",
        "Please select edges first!": "\uba3c\uc800 \uc5d0\uc9c0\ub97c \uc120\ud0dd\ud558\uc2ed\uc2dc\uc624!",
        "OmniOutset Tools": "OmniOutset \ub3c4\uad6c",
        "Smart Face Extrude": "\uc2a4\ub9c8\ud2b8 \uba74 \ub3cc\ucd9c (Face)",
        "Equidistant Edge Extrude": "\ub4f1\uac70\ub9ac \uc5d0\uc9c0 \ub3cc\ucd9c (Edge)",
        "Smart Face Extrude & Outset": "\uc2a4\ub9c8\ud2b8 \uba74 \ub3cc\ucd9c \ubc0f \uc544\uc6c3\uc14b",
        "Extrude Distance": "\ub3cc\ucd9c \uac70\ub9ac",
        "Outward Offset": "\ubc14\uae65\ucabd \uc624\ud504\uc14b \uac70\ub9ac",
        "Z Axis Offset": "Z\ucd95 \uc624\ud504\uc14b",
        "OmniOutset Face | Extrude: {0:.3f} (Up/Down) | Outset: {1:.3f} (Ctrl+L/R) | [Shift] Precision | [LMB] Confirm": "OmniOutset \uba74 | \ub3cc\ucd9c: {0:.3f} (\uc704/\uc544\ub798) | \uc544\uc6c3\uc14b: {1:.3f} (Ctrl+\uc88c/\uc6b0) | [Shift] \ubbf8\uc138 \uc870\uc815 | [\uc88c\ud074\ub9ad] \ud655\uc778",
        "OmniOutset Edge | Outset: {0:.3f} (L/R) | Z-Offset: {1:.3f} (Ctrl+Up/Down) | [Shift] Precision | [LMB] Confirm": "OmniOutset \uc5d0\uc9c0 | \uc544\uc6c3\uc14b: {0:.3f} (\uc88c/\uc6b0) | Z\ucd95: {1:.3f} (Ctrl+\uc704/\uc544\ub798) | [Shift] \ubbf8\uc138 \uc870\uc815 | [\uc88c\ud074\ub9ad] \ud655\uc778",
        "Smart OmniOutset Call": "\uc2a4\ub9c8\ud2b8 OmniOutset \ud638\ucd9c",
        "OmniOutset Shortcut Configuration": "OmniOutset \ub2e8\ucd95\ud0a4 \uc124\uc815",
        "Customize the universal hotkey for Face & Edge Extrude below:": "\uc544\ub798\uc5d0\uc11c \uba74 \ubc0f \uc5d0\uc9c0 \ub3cc\ucd9c\uc744 \uc704\ud55c \uacf5\ud1b5 \ub2e8\ucd95\ud0a4\ub97c \uc0ac\uc6a9\uc790 \uc815\uc758\ud558\uc2ed\uc2dc\uc624:",
        "No user keyconfig found.": "\uc0ac\uc6a9\uc790 \ud0a4 \uc124\uc815\uc744 \ucc3e\uc744 \uc218 \uc5c6\uc2b5\ub2c8\ub2e4.",
        "Mesh keymap not found.": "\uba54\uc2dc \ud0a4\ub9f5\uc744 \ucc3e\uc744 \uc218 \uc5c6\uc2b5\ub2c8\ub2e4.",
        "Shortcut not found. Please try restarting Blender.": "\ub2e8\ucd95\ud0a4\ub97c \ucc3e\uc744 \uc218 \uc5c6\uc2b5\ub2c8\ub2e4. Blender\ub97c \ub2e4\uc2dc \uc2dc\uc791\ud574 \ubcf4\uc2ed\uc2dc\uc624.",
    },
    contexts=(CONTEXT_DEFAULT, CONTEXT_OPERATOR),
)


dict_spanish = _entries(
    {
        "At least one face must be selected!": "Debes seleccionar al menos una cara!",
        "Please select edges first!": "Selecciona primero los bordes!",
        "OmniOutset Tools": "Herramientas OmniOutset",
        "Smart Face Extrude": "Extrusi\u00f3n Inteligente de Caras (Face)",
        "Equidistant Edge Extrude": "Extrusi\u00f3n Equidistante de Bordes (Edge)",
        "Smart Face Extrude & Outset": "Extrusi\u00f3n Inteligente de Caras y Desfase",
        "Extrude Distance": "Distancia de Extrusi\u00f3n",
        "Outward Offset": "Desplazamiento Hacia Afuera",
        "Z Axis Offset": "Desplazamiento del Eje Z",
        "OmniOutset Face | Extrude: {0:.3f} (Up/Down) | Outset: {1:.3f} (Ctrl+L/R) | [Shift] Precision | [LMB] Confirm": "OmniOutset Cara | Extrusi\u00f3n: {0:.3f} (Arriba/Abajo) | Desfase: {1:.3f} (Ctrl+Izq./Der.) | [Shift] Precisi\u00f3n | [LMB] Confirmar",
        "OmniOutset Edge | Outset: {0:.3f} (L/R) | Z-Offset: {1:.3f} (Ctrl+Up/Down) | [Shift] Precision | [LMB] Confirm": "OmniOutset Borde | Desfase: {0:.3f} (Izq./Der.) | Eje Z: {1:.3f} (Ctrl+Arriba/Abajo) | [Shift] Precisi\u00f3n | [LMB] Confirmar",
        "Smart OmniOutset Call": "Llamada Inteligente de OmniOutset",
        "OmniOutset Shortcut Configuration": "Configuraci\u00f3n de Atajos de OmniOutset",
        "Customize the universal hotkey for Face & Edge Extrude below:": "Personaliza abajo el atajo universal para la extrusi\u00f3n de caras y bordes:",
        "No user keyconfig found.": "No se encontr\u00f3 la configuraci\u00f3n de teclas del usuario.",
        "Mesh keymap not found.": "No se encontr\u00f3 el mapa de teclas de Mesh.",
        "Shortcut not found. Please try restarting Blender.": "No se encontr\u00f3 el atajo. Intenta reiniciar Blender.",
    },
    contexts=(CONTEXT_DEFAULT, CONTEXT_OPERATOR),
)


dict_french = _entries(
    {
        "At least one face must be selected!": "Vous devez s\u00e9lectionner au moins une face !",
        "Please select edges first!": "S\u00e9lectionnez d'abord des ar\u00eates !",
        "OmniOutset Tools": "Outils OmniOutset",
        "Smart Face Extrude": "Extrusion Intelligente de Face (Face)",
        "Equidistant Edge Extrude": "Extrusion \u00c9quidistante d'Ar\u00eate (Edge)",
        "Smart Face Extrude & Outset": "Extrusion Intelligente de Face et D\u00e9calage",
        "Extrude Distance": "Distance d'Extrusion",
        "Outward Offset": "D\u00e9calage vers l'Ext\u00e9rieur",
        "Z Axis Offset": "D\u00e9calage sur l'Axe Z",
        "OmniOutset Face | Extrude: {0:.3f} (Up/Down) | Outset: {1:.3f} (Ctrl+L/R) | [Shift] Precision | [LMB] Confirm": "OmniOutset Face | Extrusion : {0:.3f} (Haut/Bas) | D\u00e9calage : {1:.3f} (Ctrl+G/D) | [Shift] Pr\u00e9cision | [LMB] Confirmer",
        "OmniOutset Edge | Outset: {0:.3f} (L/R) | Z-Offset: {1:.3f} (Ctrl+Up/Down) | [Shift] Precision | [LMB] Confirm": "OmniOutset Ar\u00eate | D\u00e9calage : {0:.3f} (G/D) | Axe Z : {1:.3f} (Ctrl+Haut/Bas) | [Shift] Pr\u00e9cision | [LMB] Confirmer",
        "Smart OmniOutset Call": "Appel Intelligent OmniOutset",
        "OmniOutset Shortcut Configuration": "Configuration des Raccourcis OmniOutset",
        "Customize the universal hotkey for Face & Edge Extrude below:": "Personnalisez ci-dessous le raccourci universel pour l'extrusion des faces et des ar\u00eates :",
        "No user keyconfig found.": "Aucune configuration de touches utilisateur trouv\u00e9e.",
        "Mesh keymap not found.": "Aucun raccourci Mesh trouv\u00e9.",
        "Shortcut not found. Please try restarting Blender.": "Raccourci introuvable. Essayez de red\u00e9marrer Blender.",
    },
    contexts=(CONTEXT_DEFAULT, CONTEXT_OPERATOR),
)


dict_portuguese = _entries(
    {
        "At least one face must be selected!": "\u00c9 preciso selecionar pelo menos uma face!",
        "Please select edges first!": "Selecione primeiro as arestas!",
        "OmniOutset Tools": "Ferramentas OmniOutset",
        "Smart Face Extrude": "Extrus\u00e3o Inteligente de Faces (Face)",
        "Equidistant Edge Extrude": "Extrus\u00e3o Equidistante de Arestas (Edge)",
        "Smart Face Extrude & Outset": "Extrus\u00e3o Inteligente de Faces e Deslocamento",
        "Extrude Distance": "Dist\u00e2ncia de Extrus\u00e3o",
        "Outward Offset": "Deslocamento para Fora",
        "Z Axis Offset": "Deslocamento no Eixo Z",
        "OmniOutset Face | Extrude: {0:.3f} (Up/Down) | Outset: {1:.3f} (Ctrl+L/R) | [Shift] Precision | [LMB] Confirm": "OmniOutset Face | Extrus\u00e3o: {0:.3f} (Cima/Baixo) | Deslocamento: {1:.3f} (Ctrl+E/D) | [Shift] Precis\u00e3o | [LMB] Confirmar",
        "OmniOutset Edge | Outset: {0:.3f} (L/R) | Z-Offset: {1:.3f} (Ctrl+Up/Down) | [Shift] Precision | [LMB] Confirm": "OmniOutset Aresta | Deslocamento: {0:.3f} (E/D) | Eixo Z: {1:.3f} (Ctrl+Cima/Baixo) | [Shift] Precis\u00e3o | [LMB] Confirmar",
        "Smart OmniOutset Call": "Chamada Inteligente OmniOutset",
        "OmniOutset Shortcut Configuration": "Configura\u00e7\u00e3o de Atalhos do OmniOutset",
        "Customize the universal hotkey for Face & Edge Extrude below:": "Personalize abaixo o atalho universal para a extrus\u00e3o de faces e arestas:",
        "No user keyconfig found.": "Nenhuma configura\u00e7\u00e3o de teclas do usu\u00e1rio foi encontrada.",
        "Mesh keymap not found.": "Nenhum mapa de teclas de Mesh foi encontrado.",
        "Shortcut not found. Please try restarting Blender.": "Atalho n\u00e3o encontrado. Tente reiniciar o Blender.",
    },
    contexts=(CONTEXT_DEFAULT, CONTEXT_OPERATOR),
)


dict_russian = _entries(
    {
        "At least one face must be selected!": "\u041d\u0443\u0436\u043d\u043e \u0432\u044b\u0431\u0440\u0430\u0442\u044c \u0445\u043e\u0442\u044f \u0431\u044b \u043e\u0434\u043d\u0443 \u0433\u0440\u0430\u043d\u044c!",
        "Please select edges first!": "\u0421\u043d\u0430\u0447\u0430\u043b\u0430 \u0432\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0440\u0451\u0431\u0440\u0430!",
        "OmniOutset Tools": "\u0418\u043d\u0441\u0442\u0440\u0443\u043c\u0435\u043d\u0442\u044b OmniOutset",
        "Smart Face Extrude": "\u0423\u043c\u043d\u0430\u044f \u042d\u043a\u0441\u0442\u0440\u0443\u0437\u0438\u044f \u0413\u0440\u0430\u043d\u0438 (Face)",
        "Equidistant Edge Extrude": "\u0420\u0430\u0432\u043d\u043e\u043c\u0435\u0440\u043d\u0430\u044f \u042d\u043a\u0441\u0442\u0440\u0443\u0437\u0438\u044f \u0420\u0451\u0431\u0435\u0440 (Edge)",
        "Smart Face Extrude & Outset": "\u0423\u043c\u043d\u0430\u044f \u042d\u043a\u0441\u0442\u0440\u0443\u0437\u0438\u044f \u0413\u0440\u0430\u043d\u0438 \u0438 \u0421\u043c\u0435\u0449\u0435\u043d\u0438\u0435",
        "Extrude Distance": "\u0420\u0430\u0441\u0441\u0442\u043e\u044f\u043d\u0438\u0435 \u042d\u043a\u0441\u0442\u0440\u0443\u0437\u0438\u0438",
        "Outward Offset": "\u0421\u043c\u0435\u0449\u0435\u043d\u0438\u0435 \u041d\u0430\u0440\u0443\u0436\u0443",
        "Z Axis Offset": "\u0421\u043c\u0435\u0449\u0435\u043d\u0438\u0435 \u043f\u043e \u041e\u0441\u0438 Z",
        "OmniOutset Face | Extrude: {0:.3f} (Up/Down) | Outset: {1:.3f} (Ctrl+L/R) | [Shift] Precision | [LMB] Confirm": "OmniOutset \u0413\u0440\u0430\u043d\u044c | \u042d\u043a\u0441\u0442\u0440\u0443\u0437\u0438\u044f: {0:.3f} (\u0412\u0432\u0435\u0440\u0445/\u0412\u043d\u0438\u0437) | \u0421\u043c\u0435\u0449\u0435\u043d\u0438\u0435: {1:.3f} (Ctrl+\u041b/\u041f) | [Shift] \u0422\u043e\u0447\u043d\u043e | [\u041b\u041a\u041c] \u041f\u043e\u0434\u0442\u0432\u0435\u0440\u0434\u0438\u0442\u044c",
        "OmniOutset Edge | Outset: {0:.3f} (L/R) | Z-Offset: {1:.3f} (Ctrl+Up/Down) | [Shift] Precision | [LMB] Confirm": "OmniOutset \u0420\u0435\u0431\u0440\u043e | \u0421\u043c\u0435\u0449\u0435\u043d\u0438\u0435: {0:.3f} (\u041b/\u041f) | \u041e\u0441\u044c Z: {1:.3f} (Ctrl+\u0412\u0432\u0435\u0440\u0445/\u0412\u043d\u0438\u0437) | [Shift] \u0422\u043e\u0447\u043d\u043e | [\u041b\u041a\u041c] \u041f\u043e\u0434\u0442\u0432\u0435\u0440\u0434\u0438\u0442\u044c",
        "Smart OmniOutset Call": "\u0423\u043c\u043d\u044b\u0439 \u0412\u044b\u0437\u043e\u0432 OmniOutset",
        "OmniOutset Shortcut Configuration": "\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0430 \u0421\u043e\u0447\u0435\u0442\u0430\u043d\u0438\u0439 OmniOutset",
        "Customize the universal hotkey for Face & Edge Extrude below:": "\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u0442\u0435 \u043d\u0438\u0436\u0435 \u0443\u043d\u0438\u0432\u0435\u0440\u0441\u0430\u043b\u044c\u043d\u0443\u044e \u0433\u043e\u0440\u044f\u0447\u0443\u044e \u043a\u043b\u0430\u0432\u0438\u0448\u0443 \u0434\u043b\u044f \u044d\u043a\u0441\u0442\u0440\u0443\u0437\u0438\u0438 \u0433\u0440\u0430\u043d\u0435\u0439 \u0438 \u0440\u0451\u0431\u0435\u0440:",
        "No user keyconfig found.": "\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c\u0441\u043a\u0430\u044f \u0440\u0430\u0441\u043a\u043b\u0430\u0434\u043a\u0430 \u043a\u043b\u0430\u0432\u0438\u0448 \u043d\u0435 \u043d\u0430\u0439\u0434\u0435\u043d\u0430.",
        "Mesh keymap not found.": "\u041a\u0430\u0440\u0442\u0430 \u043a\u043b\u0430\u0432\u0438\u0448 Mesh \u043d\u0435 \u043d\u0430\u0439\u0434\u0435\u043d\u0430.",
        "Shortcut not found. Please try restarting Blender.": "\u0421\u043e\u0447\u0435\u0442\u0430\u043d\u0438\u0435 \u043a\u043b\u0430\u0432\u0438\u0448 \u043d\u0435 \u043d\u0430\u0439\u0434\u0435\u043d\u043e. \u041f\u043e\u043f\u0440\u043e\u0431\u0443\u0439\u0442\u0435 \u043f\u0435\u0440\u0435\u0437\u0430\u043f\u0443\u0441\u0442\u0438\u0442\u044c Blender.",
    },
    contexts=(CONTEXT_DEFAULT, CONTEXT_OPERATOR),
)


dict_german = _entries(
    {
        "At least one face must be selected!": "Mindestens eine Fl\u00e4che muss ausgew\u00e4hlt sein!",
        "Please select edges first!": "Bitte w\u00e4hle zuerst Kanten aus!",
        "OmniOutset Tools": "OmniOutset Werkzeuge",
        "Smart Face Extrude": "Intelligentes Fl\u00e4chen-Extrudieren (Face)",
        "Equidistant Edge Extrude": "\u00c4quidistantes Kanten-Extrudieren (Edge)",
        "Smart Face Extrude & Outset": "Intelligentes Fl\u00e4chen-Extrudieren und Offset",
        "Extrude Distance": "Extrusionsabstand",
        "Outward Offset": "Offset nach Au\u00dfen",
        "Z Axis Offset": "Z-Achsen-Offset",
        "OmniOutset Face | Extrude: {0:.3f} (Up/Down) | Outset: {1:.3f} (Ctrl+L/R) | [Shift] Precision | [LMB] Confirm": "OmniOutset Fl\u00e4che | Extrusion: {0:.3f} (Hoch/Runter) | Offset: {1:.3f} (Strg+L/R) | [Shift] Pr\u00e4zision | [LMB] Best\u00e4tigen",
        "OmniOutset Edge | Outset: {0:.3f} (L/R) | Z-Offset: {1:.3f} (Ctrl+Up/Down) | [Shift] Precision | [LMB] Confirm": "OmniOutset Kante | Offset: {0:.3f} (L/R) | Z-Offset: {1:.3f} (Strg+Hoch/Runter) | [Shift] Pr\u00e4zision | [LMB] Best\u00e4tigen",
        "Smart OmniOutset Call": "Intelligenter OmniOutset-Aufruf",
        "OmniOutset Shortcut Configuration": "OmniOutset-Tastenk\u00fcrzel",
        "Customize the universal hotkey for Face & Edge Extrude below:": "Passe unten das universelle Tastenk\u00fcrzel f\u00fcr Fl\u00e4chen- und Kanten-Extrusion an:",
        "No user keyconfig found.": "Keine Benutzer-Tastenkonfiguration gefunden.",
        "Mesh keymap not found.": "Keine Mesh-Tastenbelegung gefunden.",
        "Shortcut not found. Please try restarting Blender.": "Tastenk\u00fcrzel nicht gefunden. Bitte starte Blender neu.",
    },
    contexts=(CONTEXT_DEFAULT, CONTEXT_OPERATOR),
)


translations_dict = {
    "zh_HANS": dict_hans,
    "zh_CN": dict_hans,
    "zh_HANT": dict_hant,
    "zh_TW": dict_hant,
    "ja_JP": dict_japanese,
    "ko_KR": dict_korean,
    "es": dict_spanish,
    "es_ES": dict_spanish,
    "fr": dict_french,
    "fr_FR": dict_french,
    "pt": dict_portuguese,
    "pt_PT": dict_portuguese,
    "pt_BR": dict_portuguese,
    "ru_RU": dict_russian,
    "de": dict_german,
    "de_DE": dict_german,
}
