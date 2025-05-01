import {
  ChangeDetectionStrategy,
  Component,
  inject,
  Input,
  OnInit,
  TemplateRef,
  ViewEncapsulation,
} from '@angular/core';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { DetailsComponent } from '../details/details.component';
import { RealEstateProperty } from '../../interfaces/realEstateProperty';
import { HttpClientModule } from '@angular/common/http';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-list',
  standalone: true,
  imports: [CommonModule, HttpClientModule, DetailsComponent],
  templateUrl: './list.component.html',
  styleUrl: './list.component.css',
  // encapsulation: ViewEncapsulation.None,
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class ListComponent {
  private modalService = inject(NgbModal);
  selectedProperty: RealEstateProperty | null = null;

  @Input() properties: RealEstateProperty[] | null = null;
  @Input() loading: boolean = false;
  @Input() error: string | null = null;

  openXl(content: TemplateRef<any>, property: RealEstateProperty) {
    this.selectedProperty = property;
    this.modalService.open(content, { size: 'xl' });
  }
}
