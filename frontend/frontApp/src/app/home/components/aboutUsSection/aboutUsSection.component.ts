import { ChangeDetectionStrategy, Component } from '@angular/core';

@Component({
  selector: 'app-about-us-section',
  standalone: true,
  imports: [],
  templateUrl: './aboutUsSection.component.html',
  styleUrl: './aboutUsSection.component.css',
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class AboutUsSectionComponent { }
