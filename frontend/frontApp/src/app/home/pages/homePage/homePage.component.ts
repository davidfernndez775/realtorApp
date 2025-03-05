import { ChangeDetectionStrategy, Component } from '@angular/core';
import { ShowcardsComponent } from '../../components/showcards/showcards.component';
import { OptioncardsComponent } from '../../components/optioncards/optioncards.component';

@Component({
  selector: 'app-home-page',
  standalone: true,
  imports: [ShowcardsComponent, OptioncardsComponent],
  templateUrl: './homePage.component.html',
  styleUrl: './homePage.component.css',
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class HomePageComponent {}
