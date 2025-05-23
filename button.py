import pygame

class AnimatedButton:
    def __init__(self, rect, text, font, color_idle, color_hover, color_click):
        self.rect = pygame.Rect(rect)
        self.text = text
        self.font = font
        self.color_idle = color_idle
        self.color_hover = color_hover
        self.color_click = color_click
        self.current_color = color_idle
        self.clicked = False

        self.text_surf = font.render(text, True, (255, 255, 255))
        self.text_rect = self.text_surf.get_rect(center=self.rect.center)

    def update(self, mouse_pos, mouse_pressed,text):
        if self.rect.collidepoint(mouse_pos):
            if mouse_pressed[0]:  # Left click held
                self.current_color = self.color_click
                self.text = text
                self.text_surf = self.font.render(text, True, (255, 255, 255))
                self.text_rect = self.text_surf.get_rect(center=self.rect.center)
                self.clicked = True
            else:
                self.current_color = self.color_hover
                self.text = text
                self.text_surf = self.font.render(text, True, (255, 255, 255))
                self.text_rect = self.text_surf.get_rect(center=self.rect.center)
        else:
            self.current_color = self.color_idle
            self.text = text
            self.text_surf = self.font.render(text, True, (255, 255, 255))
            self.text_rect = self.text_surf.get_rect(center=self.rect.center)

    def draw(self, surface):
        pygame.draw.rect(surface, self.current_color, self.rect, border_radius=8)
        surface.blit(self.text_surf, self.text_rect)

    def is_clicked(self, mouse_pos, event_list):
        return self.rect.collidepoint(mouse_pos) and any(
            event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 for event in event_list
        )
