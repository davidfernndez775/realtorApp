import { Component, ChangeDetectorRef } from '@angular/core';
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
        style({ transform: 'scale(0.5)', opacity: 0 }), // Estado inicial
        animate('500ms ease-out', style({ transform: 'scale(1)', opacity: 1 })), // Estado final
      ]),
    ]),
  ],
})
export class ShowcardsComponent {
  isVisible = false; // Inicialmente oculto

  constructor(private cdr: ChangeDetectorRef) {
    setTimeout(() => {
      this.isVisible = true;
      this.cdr.markForCheck(); // 🔥 Forzar detección de cambios
    }, 10);
  }
}
