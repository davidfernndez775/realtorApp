import {
  ChangeDetectionStrategy,
  Component,
  EventEmitter,
  inject,
  Input,
  Output,
  TemplateRef,
  ViewEncapsulation,
} from '@angular/core';
import { NgbOffcanvas } from '@ng-bootstrap/ng-bootstrap';
import { NgbDropdownModule } from '@ng-bootstrap/ng-bootstrap';
import {
  FormBuilder,
  FormGroup,
  ReactiveFormsModule,
  Validators,
} from '@angular/forms';
import { RealEstateProperty } from '../../interfaces/realEstateProperty';

@Component({
  selector: 'app-search-form',
  standalone: true,
  imports: [NgbDropdownModule, ReactiveFormsModule],
  templateUrl: './searchForm.component.html',
  styleUrl: './searchForm.component.css',
  changeDetection: ChangeDetectionStrategy.OnPush,
  encapsulation: ViewEncapsulation.None,
})
export class SearchFormComponent {
  private offcanvasService = inject(NgbOffcanvas);

  counties = [
    'Broward',
    'Charlotte',
    'Collier',
    'Glades',
    'Hendry',
    'Highlands',
    'Lee',
    'Martin',
    'Miami Dade',
    'Monroe',
    'Okeechobee',
    'Palm Beach',
    'Saint Lucie',
  ];
  propertyTypes = [
    'Single Family',
    'Condo/Co-Op/Villa/Townhouse',
    'Multi-Family Income',
    'Residential Land/Boat Docks',
    'Land-Commercial/Business/Agricultural/Industrial',
    'Residential Rental',
    'Commercial/Industrial',
    'Business Brokerage',
  ];

  @Output() filtersApplied = new EventEmitter<any>();

  filterForm: FormGroup;

  constructor(private fb: FormBuilder) {
    this.filterForm = this.fb.group({
      property_type: [''],
      county: [''],
      for_rent_or_sale: [''],
      new: [false],
      price_decrease: [false],
      water_front: [false],
      price_min: [null],
      price_max: [null],
      square_ft_min: [null],
      square_ft_max: [null],
      beds_min: [null],
      beds_max: [null],
      full_baths_min: [null],
      full_baths_max: [null],
      half_baths_min: [null],
      half_baths_max: [null],
      built_min: [null],
      built_max: [null],
    });
  }

  openEnd(content: TemplateRef<any>) {
    this.offcanvasService.open(content, { position: 'end' });
  }

  applyFilters(): void {
    this.filtersApplied.emit(this.filterForm.value);
  }
}
