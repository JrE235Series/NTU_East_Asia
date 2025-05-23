import pygame

class AnimatedButton:
    def __init__(self, rect, text, font, color_idle, color_hover, color_click):
        self.rect = pygame.Rect(rect)
        self.font = font
        self.text = text
        self.color_idle = color_idle
        self.color_hover = color_hover
        self.color_click = color_click
        self.current_state = "idle"  # idle, hover, or click

        self._render_text()

    def _render_text(self):
        self.text_surf = self.font.render(self.text, True, (255, 255, 255))
        self.text_rect = self.text_surf.get_rect(center=self.rect.center)

    def set_text(self, new_text):
        self.text = new_text
        self._render_text()

    def update(self, mouse_pos, mouse_pressed):
        if self.rect.collidepoint(mouse_pos):
            if mouse_pressed[0]:  # left mouse held
                self.current_state = "click"
            else:
                self.current_state = "hover"
        else:
            self.current_state = "idle"

    def draw(self, surface):
        # Create transparent surface with alpha
        button_surface = pygame.Surface(self.rect.size, pygame.SRCALPHA)

        if self.current_state == "hover":
            pygame.draw.rect(
                button_surface,
                (255, 255, 255, 128),  # half-transparent white
                button_surface.get_rect(),
                border_radius=12       # adjust radius as needed
            )
        elif self.current_state == "click":
            pygame.draw.rect(
                button_surface,
                (*self.color_click, 128),  # fully opaque click color
                button_surface.get_rect(),
                border_radius=10
            )
        # idle: leave fully transparent

        # Blit the semi-transparent background
        surface.blit(button_surface, self.rect.topleft)

        # Draw text directly onto the parent surface (not on the button_surface)
        surface.blit(self.text_surf, self.text_rect)


    def is_clicked(self, mouse_pos, events):
        return self.rect.collidepoint(mouse_pos) and any(
            event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 for event in events
        )
