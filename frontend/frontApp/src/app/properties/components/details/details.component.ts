import { ChangeDetectionStrategy, Component } from '@angular/core';
import { NgbCarouselModule } from '@ng-bootstrap/ng-bootstrap';
import { TableDetailsComponent } from '../tableDetails/tableDetails.component';

@Component({
  selector: 'app-details',
  standalone: true,
  imports: [NgbCarouselModule, TableDetailsComponent],
  templateUrl: './details.component.html',
  styleUrl: './details.component.css',
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class DetailsComponent {
  images = [944, 1011, 984].map((n) => `https://picsum.photos/id/${n}/900/500`);
}
