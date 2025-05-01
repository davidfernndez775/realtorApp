import {
  ChangeDetectionStrategy,
  Component,
  Input,
  TemplateRef,
} from '@angular/core';
import { NgbCarouselModule } from '@ng-bootstrap/ng-bootstrap';
import { TableDetailsComponent } from '../tableDetails/tableDetails.component';
import { RealEstateProperty } from '../../interfaces/realEstateProperty';

@Component({
  selector: 'app-details',
  standalone: true,
  imports: [NgbCarouselModule, TableDetailsComponent],
  templateUrl: './details.component.html',
  styleUrl: './details.component.css',
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class DetailsComponent {
  @Input() property!: RealEstateProperty | null;
  images = [944, 1011, 984].map((n) => `https://picsum.photos/id/${n}/900/500`);
}
