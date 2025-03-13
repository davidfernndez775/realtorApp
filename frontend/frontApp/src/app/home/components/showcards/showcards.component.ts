import { Component } from '@angular/core';
import { trigger, transition, style, animate } from '@angular/animations';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-showcards',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './showcards.component.html',
  styleUrl: './showcards.component.css',
  animations: [
    trigger('intro', [
      transition(':enter', [
        // Se ejecuta cuando el elemento aparece en el DOM
        style({ transform: 'scale(0.5)', opacity: 0 }), // Estado inicial
        animate('500ms ease-out', style({ transform: 'scale(1)', opacity: 1 })), // Estado final
      ]),
    ]),
  ],
})
export class ShowcardsComponent {
  isVisible = false; // Inicialmente oculto

  constructor() {
    setTimeout(() => {
      this.isVisible = true; // Muestra el contenido después de 10ms
    }, 10);
  }
}
