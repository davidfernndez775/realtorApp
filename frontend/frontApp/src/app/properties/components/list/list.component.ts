import {
  ChangeDetectionStrategy,
  Component,
  Input,
  OnInit,
  TemplateRef,
  ViewEncapsulation,
  inject,
} from '@angular/core';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { RealEstateProperty } from '../../interfaces/realEstateProperty';
import { HttpClientModule } from '@angular/common/http';
import { CommonModule } from '@angular/common';
import { DetailModalComponent } from '../detail-modal/detail-modal.component';

@Component({
  selector: 'app-list',
  standalone: true,
  imports: [CommonModule, HttpClientModule],
  templateUrl: './list.component.html',
  styleUrl: './list.component.css',
  // encapsulation: ViewEncapsulation.None,
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class ListComponent {
  selectedProperty: RealEstateProperty | null = null;
  private modalService = inject(NgbModal);
  @Input() properties: RealEstateProperty[] | null = null;
  @Input() loading: boolean = false;
  @Input() error: string | null = null;

  openXl(property: RealEstateProperty) {
    const modalRef = this.modalService.open(DetailModalComponent, {
      size: 'xl',
    });
    modalRef.componentInstance.property = property;
  }
}
