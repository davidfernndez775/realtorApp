import { Component } from '@angular/core';
import { trigger, transition, style, animate } from '@angular/animations';
import { CommonModule } from '@angular/common';
import { ShowcardsComponent } from '../../components/showcards/showcards.component';
import { OptioncardsComponent } from '../../components/optioncards/optioncards.component';
import { ReadyToBuyComponent } from '../../components/readyToBuy/readyToBuy.component';

@Component({
  selector: 'app-business-section',
  standalone: true,
  imports: [
    CommonModule,
    ShowcardsComponent,
    OptioncardsComponent,
    ReadyToBuyComponent,
  ],
  templateUrl: './businessSection.component.html',
  styleUrl: './businessSection.component.css',
  animations: [
    trigger('intro', [
      transition(':enter', [
        style({ transform: 'scale(0.8)', opacity: 0 }),
        animate('600ms ease-out', style({ transform: 'scale(1)', opacity: 1 })),
      ]),
    ]),
  ],
})
export class BusinessSectionComponent {
  isVisible = false; // Inicialmente oculto
  animationDone = false; // Para controlar la visibilidad después de la animación

  ngOnInit() {
    setTimeout(() => {
      this.isVisible = true;
    }, 50); // Pequeño retraso antes de activar la animación
  }

  onAnimationDone() {
    this.animationDone = true; // Marca que la animación ha terminado
  }
}
