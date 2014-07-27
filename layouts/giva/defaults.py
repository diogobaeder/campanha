from mezzanine.conf import register_setting


register_setting(
    name="SITE_TITLE",
    description="Título do site.",
    editable=True,
    default='Giva 5006 PSOL',
)
register_setting(
    name="SITE_TAGLINE",
    description="Slogan do site.",
    editable=True,
    default='Frente de Esquerda',
)
