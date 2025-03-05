import { ChangeDetectionStrategy, Component } from '@angular/core';
import { ShowcardsComponent } from '../../components/showcards/showcards.component';
import { OptioncardsComponent } from '../../components/optioncards/optioncards.component';
import { WhatsappButtonComponent } from '../../../shared/components/whatsappButton/whatsappButton.component';
import { ReadyToBuyComponent } from '../../components/readyToBuy/readyToBuy.component';

@Component({
  selector: 'app-home-page',
  standalone: true,
  imports: [
    ShowcardsComponent,
    OptioncardsComponent,
    WhatsappButtonComponent,
    ReadyToBuyComponent,
  ],
  templateUrl: './homePage.component.html',
  styleUrl: './homePage.component.css',
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class HomePageComponent {}
