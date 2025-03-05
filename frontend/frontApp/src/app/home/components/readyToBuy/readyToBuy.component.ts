import { ChangeDetectionStrategy, Component } from '@angular/core';

@Component({
  selector: 'app-ready-to-buy',
  standalone: true,
  imports: [],
  templateUrl: './readyToBuy.component.html',
  styleUrl: './readyToBuy.component.css',
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class ReadyToBuyComponent { }
