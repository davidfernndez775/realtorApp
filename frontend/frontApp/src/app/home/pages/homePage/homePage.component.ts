import { ChangeDetectionStrategy, Component } from '@angular/core';
import { WhatsappButtonComponent } from '../../../shared/components/whatsappButton/whatsappButton.component';
import { AboutUsSectionComponent } from '../../sections/aboutUsSection/aboutUsSection.component';
import { CommentSectionComponent } from '../../sections/commentSection/commentSection.component';
import { BusinessSectionComponent } from '../../sections/businessSection/businessSection.component';

@Component({
  selector: 'app-home-page',
  standalone: true,
  imports: [
    BusinessSectionComponent,
    WhatsappButtonComponent,
    CommentSectionComponent,
    AboutUsSectionComponent,
  ],
  templateUrl: './homePage.component.html',
  styleUrl: './homePage.component.css',
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class HomePageComponent {}
