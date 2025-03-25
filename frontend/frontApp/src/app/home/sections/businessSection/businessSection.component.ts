import {
  ChangeDetectionStrategy,
  Component,
  ChangeDetectorRef,
} from '@angular/core';
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
  changeDetection: ChangeDetectionStrategy.OnPush,
  animations: [
    trigger('intro', [
      transition(':enter', [
        style({ transform: 'scale(0.5)', opacity: 0 }), // Estado inicial
        animate('500ms ease-out', style({ transform: 'scale(1)', opacity: 1 })), // Estado final
      ]),
    ]),
  ],
})
export class BusinessSectionComponent {
  isVisible = false; // Inicialmente oculto

  constructor(private cdr: ChangeDetectorRef) {
    setTimeout(() => {
      this.isVisible = true;
      this.cdr.markForCheck(); // 🔥 Forzar detección de cambios
    }, 10);
  }
}
