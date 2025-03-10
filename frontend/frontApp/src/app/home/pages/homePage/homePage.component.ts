import { ChangeDetectionStrategy, Component } from '@angular/core';
import { ShowcardsComponent } from '../../components/showcards/showcards.component';
import { OptioncardsComponent } from '../../components/optioncards/optioncards.component';
import { WhatsappButtonComponent } from '../../../shared/components/whatsappButton/whatsappButton.component';
import { ReadyToBuyComponent } from '../../components/readyToBuy/readyToBuy.component';
import { CommentsComponent } from '../../components/comments/comments.component';
import { AboutUsSectionComponent } from '../../components/aboutUsSection/aboutUsSection.component';

@Component({
  selector: 'app-home-page',
  standalone: true,
  imports: [
    ShowcardsComponent,
    OptioncardsComponent,
    WhatsappButtonComponent,
    ReadyToBuyComponent,
    CommentsComponent,
    AboutUsSectionComponent,
  ],
  templateUrl: './homePage.component.html',
  styleUrl: './homePage.component.css',
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class HomePageComponent {}
