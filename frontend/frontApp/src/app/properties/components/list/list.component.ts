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
import { RealEstatePropertyList } from '../../interfaces/realEstateProperty';
import { RealEstatePropertyService } from '../../services/realEstateProperty.service';
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
export class ListComponent implements OnInit {
  private modalService = inject(NgbModal);

  public properties: RealEstatePropertyList[] = [];

  openXl(content: TemplateRef<any>) {
    this.modalService.open(content, { size: 'xl' });
  }

  constructor(private realEstatePropertyService: RealEstatePropertyService) {}

  ngOnInit(): void {
    this.realEstatePropertyService
      .getPropertyList()
      .subscribe((properties) => (this.properties = properties));
  }
}
