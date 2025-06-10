import { ChangeDetectionStrategy, Component, Input } from '@angular/core';
import { NgbActiveModal } from '@ng-bootstrap/ng-bootstrap';
import { RealEstateProperty } from '../../interfaces/realEstatePropertyinterface.';
import { DetailsComponent } from '../details/details.component';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-detail-modal',
  standalone: true,
  imports: [CommonModule, DetailsComponent],
  templateUrl: './detail-modal.component.html',
  styleUrl: './detail-modal.component.css',
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class DetailModalComponent {
  @Input() property!: RealEstateProperty;

  constructor(public modal: NgbActiveModal) {}
}
