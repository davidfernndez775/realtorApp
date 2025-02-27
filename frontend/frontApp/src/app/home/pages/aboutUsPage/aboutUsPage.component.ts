import { ChangeDetectionStrategy, Component } from '@angular/core';

@Component({
  selector: 'app-about-us-page',
  standalone: true,
  imports: [],
  templateUrl: './aboutUsPage.component.html',
  styleUrl: './aboutUsPage.component.css',
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class AboutUsPageComponent { }
