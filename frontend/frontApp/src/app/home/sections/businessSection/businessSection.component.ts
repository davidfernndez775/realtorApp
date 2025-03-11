import { ChangeDetectionStrategy, Component } from '@angular/core';
import { ShowcardsComponent } from '../../components/showcards/showcards.component';
import { OptioncardsComponent } from '../../components/optioncards/optioncards.component';
import { ReadyToBuyComponent } from '../../components/readyToBuy/readyToBuy.component';

@Component({
  selector: 'app-business-section',
  standalone: true,
  imports: [ShowcardsComponent, OptioncardsComponent, ReadyToBuyComponent],
  templateUrl: './businessSection.component.html',
  styleUrl: './businessSection.component.css',
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class BusinessSectionComponent {}
