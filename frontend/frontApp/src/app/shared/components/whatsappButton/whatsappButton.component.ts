import { ChangeDetectionStrategy, Component } from '@angular/core';

@Component({
  selector: 'app-whatsapp-button',
  standalone: true,
  imports: [],
  templateUrl: './whatsappButton.component.html',
  styleUrl: './whatsappButton.component.css',
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class WhatsappButtonComponent { }
