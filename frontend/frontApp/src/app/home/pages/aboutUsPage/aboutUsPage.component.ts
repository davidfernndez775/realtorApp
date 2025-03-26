import { ChangeDetectionStrategy, Component } from '@angular/core';
import { AboutUsSectionComponent } from '../../sections/aboutUsSection/aboutUsSection.component';

@Component({
  selector: 'app-about-us-page',
  standalone: true,
  imports: [AboutUsSectionComponent],
  templateUrl: './aboutUsPage.component.html',
  styleUrl: './aboutUsPage.component.css',
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class AboutUsPageComponent {}
